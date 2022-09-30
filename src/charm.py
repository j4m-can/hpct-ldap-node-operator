#!/usr/bin/env python3
# Copyright 2022 Canonical Ltd.
# See LICENSE file for licensing details.
#
# Learn more at: https://juju.is/docs/sdk

"""LDAP node operator.
"""

import logging

from ops.main import main

from hpctinterface.relation import interface_registry
from hpctops.charm.node import NodeCharm


logger = logging.getLogger(__name__)


class HpctLDAPNodeCharm(NodeCharm):
    """Operator for cluster LDAP node."""

    def __init__(self, *args):
        super().__init__(*args)

        self.interfaces = {
            "ldap-server-ready": interface_registry.load(
                "relation-subordinate-ready", self, "ldap-server-ready"
            ),
        }

        self.setup_subordinate_relations_and_syncs(["ldap-server-ready"])


if __name__ == "__main__":
    main(HpctLDAPNodeCharm)
