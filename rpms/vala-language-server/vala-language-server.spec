Name:           vala-language-server
Summary:        Language server for the Vala programming language
Version:        0.48.4
Release:        %autorelease
License:        LGPLv2+

URL:            https://github.com/Prince781/vala-language-server
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  vala >= 0.48.12
BuildRequires:  vala-devel >= 0.48.12

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.4.4
BuildRequires:  pkgconfig(jsonrpc-glib-1.0) >= 3.28
BuildRequires:  pkgconfig(scdoc)

Requires:       libvala >= 0.48.12

Requires:       pkgconfig(gee-0.8)
Requires:       pkgconfig(glib-2.0)
Requires:       pkgconfig(gobject-introspection-1.0)
Requires:       pkgconfig(json-glib-1.0) >= 1.4.4
Requires:       pkgconfig(jsonrpc-glib-1.0) >= 3.28

Suggests:       gnome-builder


%description
Provides code intelligence for Vala (and also Genie).
Used with an editor and a plugin that supports the Language Server Protocol.


%prep
%autosetup -n %{name}-%{version}


%build
%meson -Dplugins=false
%meson_build


%install
%meson_install


%files
%license COPYING
%doc README.md

%{_bindir}/%{name}

%{_datadir}/man/man1/%{name}.1.gz


%changelog
%autochangelog