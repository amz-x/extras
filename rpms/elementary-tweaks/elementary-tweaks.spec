%global app_name pantheon-tweaks
%global srcname pantheon-tweaks-master
%global plugname pantheon-tweaks-plug
%global build_timestamp %{lua: print(os.date("%Y%m%d"))}

Name:           elementary-tweaks
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        A system settings panel for elementary

License:        GPLv3+
URL:            https://github.com/pantheon-tweaks/pantheon-tweaks
Source0:        https://github.com/pantheon-tweaks/pantheon-tweaks/archive/main.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(camel-1.2)
BuildRequires:  pkgconfig(libedataserver-1.2)
BuildRequires:  pkgconfig(libedataserverui-1.2)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
BuildRequires:  pkgconfig(webkit2gtk-web-extension-4.0)
BuildRequires:  pkgconfig(folks)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(switchboard-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)

Requires:       hicolor-icon-theme

%description
%{summary}.

%prep
%autosetup -n %{srcname}


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{plugname}

%files -f %{plugname}.lang
%license COPYING
%doc README.md

%{_libdir}/switchboard/personal/lib%{name}.so

%{_datadir}/icons/hicolor/*/categories/preferences-*.svg

%changelog

* Sun Mar 07 2021 Christopher Croues <mail@amz-x.com>
- Switched to pantheon-tweaks version

* Mon Jul 06 2020 Christopher Croues <mail@amz-x.com>
- Bumped version

* Wed Feb 05 2020 Christopher Crouse <mail@amz-x.com>
- Bumped version

* Thu Jan 02 2020 Christopher Crouse <mail@amz-x.com>
- Fix linting & bumped

* Mon Dec 09 2019 Christopher Crouse <mail@amz-x.com>
- Bumped

* Sat Oct 26 2019 Christopher Crouse <mail@amz-x.com>
- Bumped

* Mon Apr 22 2019 Christopher Crouse <mail@amz-x.com>
- Initialized spec file