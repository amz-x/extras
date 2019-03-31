%define debug_package %{nil}

Name:           antibody
Version:        4.1.1
Release:        1%{?dist}
Summary:        The fastest shell plugin manager

License:        MIT
URL:            https://github.com/getantibody/%{name}
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  git
BuildRequires:  go

%description
Antibody is a shell plugin manager made from the ground up thinking about performance

%prep

%autosetup
sed -i "25s/dev/%{version}/" "main.go"

%build 
go build .

%check
make test

%install
mkdir -p "%{buildroot}/usr/bin"
install -m 0755 "%{name}" "%{buildroot}/usr/bin/%{name}"

%files
%{_bindir}/%{name}

%license LICENSE.md
%doc README.md

%changelog
* Sun Mar 31 2019 Christopher Crouse <amz.x@protonmail.com>
- Initialized spec file
