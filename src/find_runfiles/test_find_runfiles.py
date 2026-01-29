# *******************************************************************************
# Copyright (c) 2025 Contributors to the Eclipse Foundation
#
# See the NOTICE file(s) distributed with this work for additional
# information regarding copyright ownership.
#
# This program and the accompanying materials are made available under the
# terms of the Apache License Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0
#
# SPDX-License-Identifier: Apache-2.0
# *******************************************************************************
from pathlib import Path

import pytest

from src import find_runfiles  # Assuming the new file is named find_runfiles.py

## --- Helpers to simulate environments ---


def setup_mock_repo(tmp_path: Path) -> Path:
    """Creates a dummy .git directory and returns the path."""
    repo: Path = tmp_path / "workspaces" / "process"
    repo.mkdir(parents=True)
    (repo / ".git").mkdir()
    return repo


## --- Tests ---


def test_run_incremental_pretty_path(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """
    Simulates: bazel run //process-docs:incremental
    Logic: Uses RUNFILES_DIR environment variable.
    """
    git_root: Path = setup_mock_repo(tmp_path)
    runfiles_path: Path = (
        git_root / "bazel-out/k8-fastbuild/bin/process-docs/incremental.runfiles"
    )
    runfiles_path.mkdir(parents=True)

    # In the new logic, get_runfiles_dir() returns the env var Path if it exists
    monkeypatch.setenv("RUNFILES_DIR", str(runfiles_path))

    result: Path = find_runfiles.get_runfiles_dir()
    assert result == runfiles_path
    assert result.exists()


def test_build_incremental_and_exec_it(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """
    Simulates: bazel build //process-docs:incremental &&
    bazel-bin/process-docs/incremental
    """
    git_root: Path = setup_mock_repo(tmp_path)
    bin_runfiles: Path = git_root / "bazel-bin/process-docs/incremental.runfiles"
    bin_runfiles.mkdir(parents=True)

    monkeypatch.setenv("RUNFILES_DIR", str(bin_runfiles))

    result: Path = find_runfiles.get_runfiles_dir()
    assert result == bin_runfiles


def test_outside_bazel_ide_support(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """
    Simulates: Running outside bazel (e.g., Esbonio/Sphinx).
    Logic: Falls back to git_root / "bazel-bin" / "ide_support.runfiles"
    """
    git_root: Path = setup_mock_repo(tmp_path)
    # The new logic uses Path.cwd().resolve() to find .git
    monkeypatch.chdir(git_root)
    monkeypatch.delenv("RUNFILES_DIR", raising=False)

    # Create the expected fallback path
    expected_path: Path = git_root / "bazel-bin" / "ide_support.runfiles"
    expected_path.mkdir(parents=True)

    result: Path = find_runfiles.get_runfiles_dir()
    assert result == expected_path


def test_find_git_root_via_traversal(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Tests find_git_root by walking up the tree from a specific path."""
    # Create the fake repo: /tmp/.../workspaces/process/.git
    git_root: Path = setup_mock_repo(tmp_path)
    monkeypatch.delenv("BUILD_WORKSPACE_DIRECTORY", raising=False)

    # Create a deep subdirectory and a "fake" script file inside it
    sub_dir: Path = git_root / "some" / "deep" / "path"
    sub_dir.mkdir(parents=True)
    fake_script: Path = sub_dir / "tool.py"
    fake_script.touch()

    # Pass the fake script path so the function starts searching from there
    result: Path = find_runfiles.find_git_root(starting_path=fake_script)

    assert result == git_root
    assert (result / ".git").exists()
