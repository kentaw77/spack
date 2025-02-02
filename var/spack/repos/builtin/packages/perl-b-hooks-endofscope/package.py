# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PerlBHooksEndofscope(PerlPackage):
    """Execute code after a scope finished compilation."""

    homepage = "https://metacpan.org/pod/B::Hooks::EndOfScope"
    url      = "http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/B-Hooks-EndOfScope-0.21.tar.gz"

    version('0.21', sha256='90f3580880f1d68b843c142cc86f58bead1f3e03634c63868ac9eba5eedae02c')

    depends_on('perl-sub-exporter-progressive', type=('build', 'run'))
