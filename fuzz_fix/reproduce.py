from __future__ import annotations

import os
import subprocess
import json


default_vscode_config = {
    "version": "0.2.0",
    "configurations": []
}


def check_clean_repo(repo_dir: str) -> bool:
    # Check whats in signature2ctc script
    # print helpful error message and return false is not clean
    return True


def download_input(input_artifactory_url: str) -> str:
    # later download from arti. if no token, give useful error message that describes how to 
    # set token via env. Probably also refer to 1p getting started guide
    input_path = '/tmp/input'
    with open(input_path, 'w') as f:
        f.write('123')
    return input_path


def checkout_commit(commit_id: str, repo_dir: str) -> None:
    # TODO
    return
    subprocess.check_call(['git', 'fetch'], cwd=repo_dir)
    subprocess.check_call(['git', 'checkout', commit_id])


def build_runnable(repo_dir: str) -> str:
    # subprocess.check_call(['./onep.sh', '--build'], cwd=repo_dir)
    print('Building...')
    test_data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'tests', 'test_data')
    subprocess.check_call(['make'], cwd=test_data_path)
    fuzzing_executable_path = os.path.join(test_data_path, 'runnable')
    if not os.path.isfile(fuzzing_executable_path):
        raise Exception(f'Fuzzing Executable {fuzzing_executable_path} was not build.')
    return fuzzing_executable_path


def update_vscode_debug_config(repo_dir: str, fuzzing_executable_path: str, input_path: str) -> None:
    vscode_path = os.path.join(repo_dir, '.vscode')
    if not os.path.exists(vscode_path):
        os.mkdir(vscode_path)

    config_path = os.path.join(vscode_path, 'launch.json')

    if os.path.exists(config_path):
        with open(config_path) as f:
            config = json.loads(f.read())
    else:
        config = default_vscode_config
 
    # TODO: check existing template in repro guide, add that here
    print('...TODO modify config')

    with open(config_path, 'w') as f:
        json.dump(config, f, indent=4)


def reproduce(repo_dir: str, commit_id: str, input_artifactory_url: str) -> None:
    # input_artifactory_url may just be path to folder without /input, but need prefix in case that changes
    if not check_clean_repo(repo_dir):
        return

    input_path = download_input(input_artifactory_url)

    checkout_commit(commit_id, repo_dir)

    # TODO: probably have to parse fuzzing_executable_path from input_artifactory_url
    fuzzing_executable_path = build_runnable(input_artifactory_url)

    update_vscode_debug_config(repo_dir, fuzzing_executable_path, input_path)
