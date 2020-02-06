%global appname com.github.hannesschulze.optimizer

Name:           optimizer
Summary:        Find out what's eating up your system resources and delete unnecessary files from your disk
Version:        1.2.1
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/hannesschulze/%{name}
Source:         %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libwnck-3.0)

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}

%build
%meson
%meson_build

%install
%meson_install

%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files 
%doc README.md
%license COPYING

%{_bindir}/%{appname}

%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_datadir}/locale/*/LC_MESSAGES/%{appname}.mo

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml

%changelog

* Thu Feb 06 2020 Christopher Crouse <mail@amz-x.com>
- Initial Spec