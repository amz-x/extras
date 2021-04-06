%define debug_package %{nil}

%global appname io.elementary.vala-lint

%global build_version 1
%global build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global build_name %{name}-%{build_timestamp}-%{build_version}

Name:           vala-lint
Version:        %{build_timestamp}
Release:        %{build_version}%{?dist}
Summary:        Small command line tool and library for checking Vala code files for code-style errors

License:        GPLv2+
URL:            https://github.com/vala-lang/vala-lint
Source0:        https://github.com/vala-lang/vala-lint/archive/master.tar.gz#/%{build_name}.tar.gz

BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(libvala-0.48)

%description
%{summary}.

%prep
%autosetup -n %{name}-master

%build
%meson
%meson_build

%install
%meson_install

%files

%{_bindir}/%{appname}
%{_libdir}/libvala-linter-1.0.so
%{_libdir}/libvala-linter-1.0.so.1
%{_libdir}/libvala-linter-1.0.so.1.0.0
%{_libdir}/pkgconfig/vala-linter-1.pc
%{_includedir}/vala-linter-1.0/vala-linter.h
%{_datadir}/vala/vapi/vala-linter-1.vapi

%license COPYING
%doc README.md

%changelog

* Tue Mar 09 2021 Christopher Crouse <mail@amz-x.com>
- Fix typo

* Mon Mar 08 2021 Christopher Crouse <mail@amz-x.com>
- Fix build & bumped version

* Wed Feb 05 2020 Christopher Crouse <mail@amz-x.com>
- Bumped version

* Thu Jan 02 2020 Christopher Crouse <mail@amz-x.com>
- Bumped version

* Thu Jan 02 2020 Christopher Crouse <mail@amz-x.com>
- Initialized spec file