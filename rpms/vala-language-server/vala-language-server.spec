Name:           vala-language-server
Summary:        Language server for the Vala programming language
Version:        0.48.3
Release:        %autorelease
License:        LGPLv2+

URL:            https://github.com/benwaffle/vala-language-server
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  vala >= 0.48
BuildRequires:  vala-devel >= 0.48.12

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(jsonrpc-glib-1.0) >= 3.30
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
%license COPYING
%doc README.md

%{_bindir}/%{name}

%{_libdir}/gnome-builder/plugins/vala_langserv.py
%{_libdir}/gnome-builder/plugins/vala_langserv.plugin

%{_datadir}/man/man1/%{name}.1.gz


%changelog
%autochangelog