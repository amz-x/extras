

Name:           flutter
Version:        2.2.3
Release:        1%{?dist}
Summary:        Flutter mobile app development framework.

License:        BSD
URL:            https://flutter.dev/
Source0:        https://github.com/flutter/flutter/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  bash
BuildRequires:  curl
BuildRequires:  git
BuildRequires:  zip
BuildRequires:  unzip

%description
The Flutter mobile app development framework.
Flutter allows developers to make cross-platform mobile apps with ease.

%prep
%autosetup -n %{name}-%{version}

%install
mkdir -p %{buildroot}/opt/flutter/
mkdir -p %{buildroot}%{_bindir}
cp -r %{_builddir}/%{name}-%{version}/* %{buildroot}/opt/flutter/

%files
/opt/flutter/*

%license LICENSE
%doc README.md

%post
ln -sf /opt/flutter/bin/dart    %{_bindir}/dart
ln -sf /opt/flutter/bin/flutter %{_bindir}/flutter

%changelog

* Wed Aug 18 2021 Christopher Crouse <mail@amz-x.com>
- Updated spec file

* Sun Jul 18 2021 Christopher Crouse <mail@amz-x.com>
- Initialized spec file