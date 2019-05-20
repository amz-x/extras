# AMZ's Personal RPM Repository

Personal collection of Fedora RPM Specs & Sources

## Package Build Statuses

Package 			| Description 								| Status
---             	| ---										| ---
antibody 			| ZSH Shell Plugin Manager					| ![rpmbuild](https://copr.fedorainfracloud.org/coprs/amz/extras/package/antibody/status_image/last_build.png)
elementary-mail 	| Pantheon Email Client                     | ![rpmbuild](https://copr.fedorainfracloud.org/coprs/amz/extras/package/elementary-mail/status_image/last_build.png)
elementary-tweaks   | System Configuration Tool                 | ![rpmbuild](https://copr.fedorainfracloud.org/coprs/amz/extras/package/elementary-tweaks/status_image/last_build.png)
protonvpn-cli		| Proton VPN CLI							| ![rpmbuild](https://copr.fedorainfracloud.org/coprs/amz/extras/package/protonvpn-cli/status_image/last_build.png)
stsdc-monitor       | Pantheon System Monitor Application       | ![rpmbuild](https://copr.fedorainfracloud.org/coprs/amz/extras/package/stsdc-monitor/status_image/last_build.png)


/*

%global srcname	aesop
%global appname	com.github.lainsce.aesop

Name:			elementary-pdf-viewer
Version:        1.1.1
Release:        1%{?dist}
Summary:        The simplest PDF viewer around

License:        GPLv3+   
URL:            https://github.com/lainsce/%{srcname}
Source0:        https://github.com/lainsce/%{srcname}/archive/1.1.1.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(granite) >= 5.2.0
BuildRequires:	pkgconfig(poppler-glib)

Requires:       hicolor-icon-theme

%description
%{summary}.

%prep
%autosetup -n %{srcname}-%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%{_bindir}/%{appname}

*/