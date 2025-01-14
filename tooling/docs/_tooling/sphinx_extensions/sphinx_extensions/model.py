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
need_type_info = {
    "workproduct": {
        "req_opt": [
            ("id", "^WP_.*$"),
            ("status", "^(draft|valid|invalid|volatile)$"),
            ("tags", "^.*$"),
            ("relevant", "^.*$"),
            ("compliance-wp", "^.*$"),
        ],
    },
    "workflow": {
        "req_opt": [
            ("id", "^WF_.*$"),
            # "tags", #TO Remove comment when process are fixed
            # "responsible", #TO Remove comment when process are fixed
            ("approver", "^.*$"),
            ("supporter", "^.*$"),
            ("input", "^.*$"),
            ("output", "^.*$"),
            ("guidance", "^.*$"),
            ("executes", "^.*$"),
            ("compliance-wf", "^.*$"),
        ],
    },
    "guidance": {
        "req_opt": [
            ("id", "^GD_.*$"),
        ],
    },
    "gd_req": {
        "req_opt": [
            ("id", "^GD_REQ__[0-9a-z_]*$"),
        ],
    },
    "gd_temp": {
        "req_opt": [
            ("id", "^GD_TEMP__[0-9a-z_]*$"),
        ],
    },
    "gd_chklst": {
        "req_opt": [
            ("id", "^GD_CHKLST__[0-9a-z_]*$"),
        ],
    },
    "gd_guidl": {
        "req_opt": [
            ("id", "^GD_GUIDL__[0-9a-z_]*$"),
        ],
    },
    "gd_concept": {
        "req_opt": [
            ("id", "^GD_CONCEPT__[0-9a-z_]*$"),
        ],
    },
    "gd_howto": {
        "req_opt": [
            ("id", "^GD_HOWTO__[0-9a-z_]*$"),
        ],
    },
    "role": {
        "req_opt": [
            ("id", "^RL_.*$"),
        ],
    },
    "team": {
        "req_opt": [
            ("id", "^TE_.*$"),
        ],
    },
    "phase": {
        "req_opt": [
            ("id", "^PH_.*$"),
        ],
    },
    "milestone": {
        "req_opt": [
            ("id", "^MS_.*$"),
        ],
    },
    "process": {
        "req_opt": [
            ("id", "^PR_.*$"),
        ],
    },
    "document": {
        "req_opt": [
            ("id", "^DOC__.*$"),
            ("status", "^(draft|valid|invalid|volatile)$"),
            ("safety", "^.*$"),
            ("compliance-gd", "^GD_.*$"),
        ],
    },
    "req": {
        "req_opt": [
            ("id", "^R_.*$"),
            ("status", "^(draft|valid|invalid)$"),  # TODO Why draft as well?
        ]
    },
    "feat_req": {
        "req_opt": [
            ("id", "^FEAT_REQ__.*$"),
            ("reqtype", "^(Functional|Interface|Process|Legal|Non-Functional)$"),
            ("security", "^(YES|NO)$"),
            ("safety", "^(QM|ASIL_B|ASIL_D)$"),
            ("status", "^(valid|invalid)$"),
            ("satisfies", "^STKH_REQ__.*$"),
        ],
    },
    "comp_req": {
        "req_opt": [
            ("id", "^COMP_REQ__.*$"),
            ("reqtype", "^(Functional|Interface|Process|Legal|Non-Functional)$"),
            ("security", "^(YES|NO)$"),
            ("safety", "^(QM|ASIL_B|ASIL_D)$"),
            ("status", "^(valid|invalid)$"),
            ("satisfies", "^FEAT_REQ__.*$"),
        ],
    },
    "tool_req": {
        "req_opt": [
            ("id", "^TOOL_REQ__.*$"),
            ("reqtype", "^(Functional|Interface|Process|Legal|Non-Functional)$"),
            ("security", "^(YES|NO)$"),
            ("safety", "^(QM|ASIL_B|ASIL_D)$"),
            ("status", "^(valid|invalid)$"),
            ("satisfies", "^GD_.*$"),
        ],
    },
    "stkh_req": {
        "req_opt": [
            ("id", "^STKH_REQ__.*$"),
            ("reqtype", "^(Functional|Interface|Process|Legal|Non-Functional)$"),
            ("security", "^(YES|NO)$"),
            ("safety", "^(QM|ASIL_B|ASIL_D)$"),
            ("status", "^(valid|invalid)$"),
            ("rationale", "^.*$"),
        ],
    },
    "aou": {
        "req_opt": [
            ("id", "^AOU__.*$"),
            ("reqtype", "^(Functional|Interface|Process|Legal|Non-Functional)$"),
            ("security", "^(YES|NO)$"),
            ("safety", "^(QM|ASIL_B|ASIL_D)$"),
            ("status", "^(valid|invalid)$"),
        ],
    },
    "feat_arc_sta": {
        "req_opt": [
            ("id", "^FEAT_ARC_STA__.*$"),
            ("security", "^(YES|NO)$"),
            ("safety", "^(QM|ASIL_B|ASIL_D)$"),
            ("status", "^(valid|invalid)$"),
            ("satisfies", "^FEAT_REQ__.*$"),
        ],
    },
    "feat_arc_dyn": {
        "req_opt": [
            ("id", "^FEAT_ARC_DYN__.*$"),
            ("security", "^(YES|NO)$"),
            ("safety", "^(QM|ASIL_B|ASIL_D)$"),
            ("status", "^(valid|invalid)$"),
            ("satisfies", "^FEAT_REQ__.*$"),
        ],
    },
    "feat_arc_int": {
        "req_opt": [
            ("id", "^FEAT_ARC_INT__.*$"),
            ("security", "^(YES|NO)$"),
            ("safety", "^(QM|ASIL_B|ASIL_D)$"),
            ("status", "^(valid|invalid)$"),
            ("satisfies", "^FEAT_REQ__.*$"),
        ],
    },
    "comp_arc_sta": {
        "req_opt": [
            ("id", "^COMP_ARC_STA__.*$"),
            ("security", "^(YES|NO)$"),
            ("safety", "^(QM|ASIL_B|ASIL_D)$"),
            ("status", "^(valid|invalid)$"),
            ("satisfies", "^COMP_REQ__.*$"),
        ],
    },
    "comp_arc_dyn": {
        "req_opt": [
            ("id", "^COMP_ARC_DYN__.*$"),
            ("security", "^(YES|NO)$"),
            ("safety", "^(QM|ASIL_B|ASIL_D)$"),
            ("status", "^(valid|invalid)$"),
            ("satisfies", "^COMP_REQ__.*$"),
        ],
    },
    "comp_arc_int": {
        "req_opt": [
            ("id", "^COMP_ARC_INT__.*$"),
            ("security", "^(YES|NO)$"),
            ("safety", "^(QM|ASIL_B|ASIL_D)$"),
            ("status", "^(valid|invalid)$"),
            ("satisfies", "^COMP_REQ__.*$"),
        ],
    },
}
