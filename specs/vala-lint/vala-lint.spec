%global appname io.elementary.vala-lint
%global libname libvala-linter-1.0.so
%global build_timestamp %{lua: print(os.date("%Y%m%d"))}

%global __provides_exclude_from ^%{_libdir}/%{libname}

Name:           vala-lint
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        Small command line tool and library for checking Vala code files for code-style errors

License:        GPLv2+
URL:            https://github.com/vala-lang/%{name}
Source0:        https://github.com/vala-lang/%{name}/archive/master.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  vala-devel
BuildRequires:  glib2-devel

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
%{_libdir}/%{libname}

%license COPYING
%doc README.md

%changelog

* Thu Jan 02 2020 Christopher Crouse <mail@amz-x.com>
- Initialized spec file