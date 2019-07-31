%define debug_package %{nil}

Name:           antibody
Version:        4.1.2
Release:        1%{?dist}
Summary:        ZSH shell plugin manager

License:        MIT
URL:            https://github.com/getantibody/%{name}
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  git
BuildRequires:  go

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}

%build 
go build .

%install
mkdir -p "%{buildroot}/usr/bin"
install -m 0755 "%{name}" "%{buildroot}/usr/bin/%{name}"

%files
%{_bindir}/%{name}

%license LICENSE.md
%doc README.md

%changelog
* Wed July 31 2019 Christopher Crouse <mail@amz-x.com>
- Bumped version

* Mon Apr 22 2019 Christopher Crouse <mail@amz-x.com>
- Updated spec file

* Sun Mar 31 2019 Christopher Crouse <mail@amz-x.com>
- Initialized spec file
