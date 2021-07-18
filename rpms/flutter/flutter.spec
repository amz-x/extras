

Name:           flutter
Version:        2.2.3
Release:        1%{?dist}
Summary:        Flutter mobile app development framework.

License:        BSD
URL:            https://flutter.dev/
Source0:        https://github.com/flutter/flutter/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

%description
The Flutter mobile app development framework.
Flutter allows developers to make cross-platform mobile apps with ease.

%prep
%autosetup

%install
cp -r %{buildroot}/%{_exec_prefix} %{buildroot}
mkdir -p %{buildroot}/etc
touch %{buildroot}/etc/profile
echo "EXPORT PATH=/flutter/bin:$PATH" >> %{buildroot}/etc/profile

%changelog

* Sun Jul 18 2021 Christopher Crouse <mail@amz-x.com>
- Initialized spec file