# *******************************************************************************
# Copyright (c) 2024 Contributors to the Eclipse Foundation
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

# Define project specific needs directives

needs_types = [
    # Requirements
    dict(
        directive="stkh_req",
        title="Stakeholder requirements",
        prefix="STKH_REQ__",
        color="#BFD8D2",
        style="node",
    ),
    dict(
        directive="tool_req",
        title="Tool Requirements",
        prefix="TOOL_REQ__",
        color="#BFD8D2",
        style="node",
    ),
    # Process
    dict(
        directive="req",  # = std_req
        title="Requirement",
        prefix="R_",
        color="#BFD8D2",
        style="node",
    ),
    dict(
        directive="role",  # = Einzelne Leute der Codeowner Gruppe
        title="Role",
        prefix="RL_",
        color="#DCB239",
        style="actor",
    ),
    dict(
        directive="team",  # = Codeowners
        title="Team",
        prefix="TE_",
        color="#DCB239",
        style="node",
    ),
    dict(
        directive="workproduct",  # = work_product
        title="Workproduct",  # = Work Product
        prefix="WP__",
        color="#DDDD00",
        style="artifact",
    ),
    dict(
        directive="workflow",
        title="Workflow",
        prefix="WF__",
        color="#FFFF00",
        style="process",
    ),
    dict(
        directive="process",
        title="Process",
        prefix="PR__",
        color="#DCB239",
        style="frame",
    ),
    dict(
        directive="guidance",
        title="Guidance",
        prefix="GD__",
        color="#DCB239",
        style="file",
    ),
    dict(
        directive="gd_req",
        title="Process Requirement",
        prefix="GD_REQ__",
        color="#DCB239",
        style="file",
    ),
    dict(
        directive="gd_temp",
        title="Process Template",
        prefix="GD_TEMP__",
        color="#DCB239",
        style="file",
    ),
    dict(
        directive="gd_chklst",
        title="Process Checklist",
        prefix="GD_CHKLST__",
        color="#DCB239",
        style="file",
    ),
    dict(
        directive="gd_guidl",
        title="Process Guideline",
        prefix="GD_GUIDL__",
        color="#DCB239",
        style="file",
    ),
    dict(
        directive="document",
        title="Document",
        prefix="DOC__",
        color="#DCB239",
        style="file",
    ),
]

# Define extra options for needs object
needs_extra_options = [
    "security",
    "safety",
    "level",
    "rationale",
    "mitigated_by",
    "reqtype",
    "codelink",
    "testlink",
    "reqcovered",
    "testcovered",
]

needs_extra_links = [
    # TODO: Refer process document for the usage of links
    {
        "option": "satisfies",
        "incoming": "is satisfied by",
        "outgoing": "satisfies",
        "style_start": "-up",
        "style_end": "->",
    },
    {
        "option": "implements",
        "incoming": "implements by",
        "outgoing": "implements",
    },
    # process links
    {  # team -> role
        "option": "contains",
        "incoming": "is part of",
        "outgoing": "consists of",
    },
    {  # workflow -> role
        "option": "responsible",
        "incoming": "is reponsible for",
        "outgoing": "responsible",
    },
    {  # workflow -> role
        "option": "approver",
        "incoming": "is approver for",
        "outgoing": "approving",
    },
    {  # workflow -> role
        "option": "supporter",
        "incoming": "is supporter for",
        "outgoing": "supporting",
    },
    {  # process -> role
        "option": "owner",
        "incoming": "is process owner for",
        "outgoing": "process owner",
    },
    {  # process -> workflow
        "option": "includes",
        "incoming": "is included in",
        "outgoing": "includes workflow",
    },
    {  # workflow -> workproduct
        "option": "output",
        "incoming": "is output from",
        "outgoing": "has output",
    },
    {  # workflow -> workproduct
        "option": "input",
        "incoming": "is input from",
        "outgoing": "has input",
    },
    {  # workflow -> guidance
        "option": "guidance",
        "incoming": "is guiding",
        "outgoing": "has guidance",
    },
    {  # workproduct -> req
        "option": "compliance-wp",
        "incoming": "complies to",
        "outgoing": "is complying with",
    },
    {  # guidance -> req
        "option": "compliance-gd",
        "incoming": "complies to",
        "outgoing": "is complying with",
    },
]
