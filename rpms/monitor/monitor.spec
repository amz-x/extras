%define debug_package %{nil}

Name:           monitor
Version:        0.9.2
Release:        1%{?dist}
Summary:        Manage processes and monitor system resources

License:        LGPLv2+
URL:            https://github.com/stsdc/monitor
Source0:        https://github.com/stsdc/monitor/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite) >= 5.3.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libbamf3)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(wingpanel)

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}

%build

# Remove subprojects folder
# rm -r ./subprojects

%meson
%meson_build

%install
%meson_install

%files

%{_bindir}/%{name}

%license COPYING
%doc README.md

%changelog

* Tue Mar 09 2021 Christopher Crouse <mail@amz-x.com>
- Initialized spec file