%define debug_package %{nil}

Name:           indicator-application
Version:        12.10.0
Release:        1%{?dist}
Summary:        Indicator to take menus from applications and place them in the panel

License:        GPLv3
URL:            https://launchpad.net/indicator-application/
Source0:        https://launchpad.net/indicator-application/12.10/%{version}/+download/%{name}-%{version}.tar.gz

BuildRequires:  automake
BuildRequires:  autoconf

BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(indicator3-0.4)
BuildRequires:  pkgconfig(appindicator3-0.1)

%description
%{summary}.

%prep

%autosetup -n %{name}-%{version}
%build
# Fix build
sed -i 's/-Werror//' %{_builddir}/%{name}-%{version}/{src,tests}/Makefile.{am,in}

%configure

%install
make DESTDIR=%{buildroot} install

%files

%{_libdir}/indicators3/7/libapplication.*
%{_libexecdir}/%{name}-service
%{_datadir}/dbus-1/services/%{name}.service
%{_datadir}/%{name}/ordering-override.keyfile

%doc README
%license COPYING

%changelog

* Wed Jul 14 2021 Christopher Crouse <mail@amz-x.com>
- Initialized spec file