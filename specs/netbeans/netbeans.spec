Name:           netbeans
Version:        11.0
Release:        1%{?dist}
Summary:        Apache NetBeans is an open source development environment, tooling platform, and application framework

License:        Apache-2.0
URL:            https://github.com/apache/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  git
BuildRequires:	ant
BuildRequires:	java-11-openjdk
BuildRequires:	java-11-openjdk-devel

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}

%build
ant -quiet -Djavac.compilerargs=-nowarn -Dbuild.compiler.deprecation=false

%install


%files
%{_bindir}/%{name}

%license LICENSE
%doc README.md

%changelog
* Thu Aug 22 2019 Christopher Crouse <mail@amz-x.com>
- Initialized spec file
