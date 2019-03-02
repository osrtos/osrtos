import sys
import os
from time import sleep

import dateutil.parser
from github import Github, UnknownObjectException
import svn.remote
import yaml
import re
from distutils.version import StrictVersion
from os import listdir, path
from os.path import isfile, join
import inspect
from svn.exception import SvnException


def fetch_github_repo_info(name):
    token = os.getenv('GITHUB_TOKEN', '')
    g = Github(token)

    last_release_time = None
    last_release_version = None
    last_commit_time = None
    try:
        repo = g.get_repo(name)
    except UnknownObjectException:
        print("Error not github: ", name)
        return [None, None, None]

    try:
        release = repo.get_latest_release()
        last_release_time = release.created_at
        last_release_version = release.tag_name
    except UnknownObjectException:
        # print("Error, cannot fetch source github")
        pass
    if last_release_version is None:
        try:
            tags = repo.get_tags()
            if tags:
                for tag in tags:
                    last_release_version = tag.name
                    break
        except UnknownObjectException:
            # print("Error, cannot fetch source github")
            pass

    branch = repo.get_branch(repo.default_branch)
    last_commit_id = branch.commit
    last_commit = repo.get_commit(last_commit_id.sha)
    last_commit_time = last_commit.last_modified
    return [last_release_time, last_release_version, dateutil.parser.parse(last_commit_time)]


def fetch_sourceforge_repo_info(name):
    last_release_time = None
    last_release_version = StrictVersion('0.0.0')
    last_release_version_string = None
    last_commit_time = None
    try:
        sourceforge_svn = svn.remote.RemoteClient("https://svn.code.sf.net/p/"+name+"/code/")
        last_commit = next(sourceforge_svn.log_default(limit=1))
        last_commit_time = last_commit.date
        root_paths = sourceforge_svn.list()
        for path_item in root_paths:
            if 'tags' in path_item:
                tags_paths = sourceforge_svn.list(rel_path=path_item)
                for tag_item in tags_paths:
                    re_result = re.search(r'([\d.]+)', tag_item)
                    if re_result:
                        try:
                            if StrictVersion(re_result.group(0)) > last_release_version:
                                last_release_version = StrictVersion(re_result.group(0))
                                last_release_version_string = tag_item
                        except ValueError:
                            pass

        if last_release_version_string:
            last_release_commit = sourceforge_svn.log_default(rel_filepath="tags/"+last_release_version_string, limit=1)
            last_release_version_string = last_release_version_string.strip(' /')
            if last_release_commit:
                last_release_time = next(last_release_commit).date
    except SvnException:
        print("Error, cannot fetch source sourceforge svn")
        pass
    return [last_release_time, last_release_version_string, last_commit_time]


def fetch_and_update(md_file):
    with open(md_file, 'r+') as f:
        content = f.read()
        if not content:
            return False
        splits = content.split(sep='---', maxsplit=3)
        if not splits:
            return False
        if splits[1] is None:
            return False
        header = yaml.load(splits[1])
        code_url = header['code-url']
        if "github.com" in code_url:
            # print("Project from github")
            code_url_splits = code_url.split('/')
            org = None
            prj = None
            for split in reversed(code_url_splits):
                if not len(split):
                    continue
                if prj is None:
                    prj = split
                else:
                    org = split
                    project_name = org + '/' +prj
                    release_time, release_version, last_updated = fetch_github_repo_info(project_name)
                    print(project_name, release_time, release_version, last_updated)
                    if release_time:
                        header['last-updated'] = release_time.strftime("%Y-%m-%d")
                    elif last_updated:
                        header['last-updated'] = last_updated.strftime("%Y-%m-%d")
                    if release_version:
                        header['version'] = release_version
                    break

        elif "sourceforge.net" in code_url:
            # print("Project from sourceforge")
            code_url_splits = code_url.split('/')
            for split in reversed(code_url_splits):
                if len(split):
                    # print("Project name: ", split)
                    release_time, release_version, last_updated = fetch_sourceforge_repo_info(split)
                    print(split, release_time, release_version, last_updated)
                    if release_time:
                        header['last-updated'] = release_time.strftime("%Y-%m-%d")
                    elif last_updated:
                        header['last-updated'] = last_updated.strftime("%Y-%m-%d")
                    if release_version:
                        header['version'] = release_version
                    break
        else:
            f.close()
            print("Error, cannot fetch ", header['title'], " source:", code_url)
            return False
        splits[1] = '\r\n'+yaml.dump(header, default_flow_style=False)
        new_content = '---'.join(splits)
        f.seek(0)
        f.write(new_content)
        f.truncate()
        f.close()


rtos_dir = path.realpath(path.dirname(inspect.getfile(inspect.currentframe()))+'/../content/rtos')
for f in listdir(rtos_dir):
    if isfile(rtos_dir + '/' + f):
        fetch_and_update(rtos_dir + '/' + f)

libraries_dir = path.realpath(path.dirname(inspect.getfile(inspect.currentframe()))+'/../content/library')
for f in listdir(libraries_dir):
    if isfile(libraries_dir + '/' + f):
        fetch_and_update(libraries_dir + '/' + f)

# print(fetch_and_update("/home/yplam/work/osrtos/content/rtos/funkos.md"))
