%{?scl:%scl_package nodejs-aws4}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global npm_name aws4

Name:       %{?scl_prefix}nodejs-%{npm_name}
Version:        1.4.1
Release:        2%{?dist}
Summary:    Signs and prepares requests using AWS Signature Version 4
License:    MIT
URL:        https://github.com/mhart/aws4.git
Source0:    http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}nodejs-devel
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
Signs and prepares requests using AWS Signature Version 4

%prep
%setup -q -n package

rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr *.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
# If any binaries are included, symlink them to bindir here


%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
#not running tests in RHSCL
%endif

%files
%{nodejs_sitelib}/%{npm_name}

%doc LICENSE
%doc README.md

%changelog
* Wed Jan 18 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.4.1-2
- Copy all js files in %%install

* Thu Jan 05 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.4.1-1
- Updated with script

* Tue Sep 20 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.3.2-2
- Initial build

