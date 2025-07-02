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
# ***************************************************
import os
import re
from sphinx.application import Sphinx
from typing import Any, Dict, List

def setup(app: Sphinx) -> Dict[str, Any]:
    """
    Sphinx extension setup function.
    """
    app.add_config_value('rust_needs_source_path', '../src', 'env')
    app.connect('builder-inited', scan_rust_for_needs)
    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }

def scan_rust_for_needs(app: Sphinx) -> None:
    """
    Scans Rust source files for needs blocks and generates an .rst file.
    """
    rust_dir: str = os.path.abspath(os.path.join(app.confdir, app.config.rust_needs_source_path))
    blocks: List[str] = []
    for root, _, files in os.walk(rust_dir):
        for file in files:
            if file.endswith('.rs'):
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, encoding='utf-8') as f:
                        content = f.read()
                    blocks += extract_needs_blocks(content)
                except Exception as e:
                    print(f"Could not read {full_path}: {e}")
    target_rst: str = os.path.join(app.confdir, '_rust_needs_autogen.rst')
    try:
        with open(target_rst, 'w', encoding='utf-8') as f:
            for block in blocks:
                f.write(block)
                f.write('\n\n')
    except Exception as e:
        print(f"Could not write {target_rst}: {e}")

    index_rst: str = os.path.join(app.confdir, 'index.rst')
    if os.path.exists(index_rst):
        try:
            with open(index_rst, encoding='utf-8') as f:
                index_content = f.read()
            if '_rust_needs_autogen' not in index_content:
                index_content = index_content.replace(
                    '.. toctree::', '.. toctree::\n   _rust_needs_autogen\n'
                )
                with open(index_rst, 'w', encoding='utf-8') as f:
                    f.write(index_content)
        except Exception as e:
            print(f"Could not update {index_rst}: {e}")

def extract_needs_blocks(content: str) -> List[str]:
    """
    Extracts needs blocks from Rust source file content.
    """
    needs_blocks: List[str] = []
    # Matches blocks starting with /// .. dd_sta:: or .. dd_dyn:: and following /// lines
    pattern = re.compile(
        r'(?:(?<=\n)|^)[ \t]*///[ \t]*(\.\. (dd_sta|dd_dyn)::[^\n]*\n'
        r'(?:[ \t]*///[^\n]*\n)*)', re.MULTILINE
    )
    for match in pattern.finditer(content):
        block: str = match.group(1)
        block = re.sub(r'^[ \t]*///[ ]?', '', block, flags=re.MULTILINE)
        needs_blocks.append(block)
    return needs_blocks
