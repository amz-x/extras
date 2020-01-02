# AMZ's Personal RPM Repository

Personal collection of Fedora RPM Specs & Sources

## Package Build Statuses

Package                 | Description                               | Status
---                     | ---                                       | ---
antibody                | ZSH Shell Plugin Manager                  | ![rpmbuild](https://copr.fedorainfracloud.org/coprs/amz/extras/package/antibody/status_image/last_build.png)
elementary-mail         | Pantheon Email Client                     | ![rpmbuild](https://copr.fedorainfracloud.org/coprs/amz/extras/package/elementary-mail/status_image/last_build.png)
elementary-tweaks       | System Configuration Tool                 | ![rpmbuild](https://copr.fedorainfracloud.org/coprs/amz/extras/package/elementary-tweaks/status_image/last_build.png)
ubuntu-family-fonts     | Ubuntu Family Fonts                       | ![rpmbuild](https://copr.fedorainfracloud.org/coprs/amz/extras/package/ubuntu-family-fonts/status_image/last_build.png)

## Building Packages

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
