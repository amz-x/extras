%define debug_package %{nil}

Name:           aws-sam-cli
Version:        1.1.0
Release:        1%{?dist}
Summary:        AWS Serverless Application Model (SAM) CLI

License:        ASL 2.0 and MIT
URL:            https://github.com/awslabs/aws-sam-cli
Source0:        %{pypi_source}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-docutils
Requires:       python3-boto3

Recommends:     groff

%{?python_provide:%python_provide python3-%{name}}

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version} -p 1

%build
%py3_build

%install
%py3_install

%files
%doc README.md
%license LICENSE
%{_bindir}/sam
%{python3_sitelib}/aws_sam_cli-*.egg-info/
%{python3_sitelib}/samcli

