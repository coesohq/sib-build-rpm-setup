build-rpm-setup
===============

This role creates rpmbuild directory structure, tarballs the git repo, and
modifies rpm spec file before building.

Requirements
------------

Tested to run on Linux, FreeBSD, and OS X. Windows is not supported.

Role Variables
--------------

* build_dependency_pkgs
* installed_packages
* artifact_name
* source_tarball_name
* source_tarball_dir

Dependencies
------------

* spec_file
* spec_file_dir
* rpmbuild_dir
* sources_dir
* new_version - from role coesohq.sib-synthesize-vars
* git_path - from role coesohq.sib-synthesize-vars

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: coesohq.sib-build-rpm-setup,
             spec_file: "project_name.spec",
             spec_file_dir: "{{ git_path }}" }

License
-------

MIT

Author Information
------------------

Hamza Sheikh
