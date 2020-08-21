# AMZ's Extras RPM Repository

Extra collection of Fedora RPM Specs, Sources & Packages

## Table of Contents

1. [Package Build Statuses](#package-build-statuses)
2. [COPR Repository Installation](#copr-repository-installation)
3. [Building New Packages](#building-new-packages)

### Package Build Statuses

Package                 | Description                               | Status
---                     | ---                                       | ---
antibody                | ZSH Shell Plugin Manager                  | ![rpmbuild](https://copr.fedorainfracloud.org/coprs/amz/extras/package/antibody/status_image/last_build.png)
elementary-mail         | Pantheon Email Client                     | ![rpmbuild](https://copr.fedorainfracloud.org/coprs/amz/extras/package/elementary-mail/status_image/last_build.png)
elementary-tweaks       | System Configuration Tool                 | ![rpmbuild](https://copr.fedorainfracloud.org/coprs/amz/extras/package/elementary-tweaks/status_image/last_build.png)
ubuntu-family-fonts     | Ubuntu Family Fonts                       | ![rpmbuild](https://copr.fedorainfracloud.org/coprs/amz/extras/package/ubuntu-family-fonts/status_image/last_build.png)
vala-language-server    | Vala Language Server                      | ![rpmbuild](https://copr.fedorainfracloud.org/coprs/amz/extras/package/vala-language-server/status_image/last_build.png)
vala-lint               | Vala Language Linter                      | ![rpmbuild](https://copr.fedorainfracloud.org/coprs/amz/extras/package/vala-lint/status_image/last_build.png)

### COPR Repository Installation

Enable COPR repository for Fedora

```bash
dnf copr enable amz/extras
```

### Setting Up RPM Build Directory

```bash
rpmdev-setuptree
```

### Building New Packages

Install package dependencies

```bash
sudo dnf builddep package.spec
```

Fetch required assets / sources

```bash
spectool -g -R package.spec
```

Build RPM package

```bash
rpmbuild -ba package.spec
```
