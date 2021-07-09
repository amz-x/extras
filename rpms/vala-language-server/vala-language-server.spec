%define debug_package %{nil}

Name:           vala-language-server
Version:        0.48.3
Release:        1%{?dist}
Summary:        Code Intelligence for Vala

License:        LGPLv2+
URL:            https://github.com/benwaffle/vala-language-server
Source0:        https://github.com/benwaffle/vala-language-server/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  vala >= 0.48.3
BuildRequires:  vala-devel >= 0.48.3
BuildRequires:  gcc
BuildRequires:  cmake

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(jsonrpc-glib-1.0) >= 3.28
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(scdoc)

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}

%build
%meson
%meson_build

%install
%meson_install

%files

%{_bindir}/%{name}
%{_libdir}/gnome-builder/plugins/vala_langserv.py
%{_libdir}/gnome-builder/plugins/vala_langserv.plugin

%{_datadir}/man/man1/vala-language-server.1.gz

%license COPYING
%doc README.md

%changelog

* Fri Jul 09 2021 Christopher Crouse <mail@amz-x.com>
- New version bump

* Tue Mar 09 2021 Christopher Crouse <mail@amz-x.com>
- Fix typo

* Mon Mar 08 2021 Christopher Crouse <mail@amz-x.com>
- Fixed build with new version 

* Wed Feb 05 2020 Christopher Crouse <mail@amz-x.com>
- Bumped version

* Thu Jan 02 2020 Christopher Crouse <mail@amz-x.com>
- Initialized spec file