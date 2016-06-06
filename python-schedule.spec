# vim: foldmethod=marker

%global python_package_name schedule
%global python_setup setup.py

Name:           python-schedule

# see HISTORY.rst
Version:        0.3.2
Release:        1%{?dist}

# {{{1 package meta-data
Summary:        Python job scheduling for humans

Group:          Development/Libraries
Vendor:         doubledog.org
License:        MIT
URL:            http://www.doubledog.org/git/%{name}/
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  python2-devel

Requires:       python2

%description
An in-process scheduler for periodic jobs that uses the builder pattern for
configuration. Schedule lets you run Python functions (or any other callable)
periodically at pre-determined intervals using a simple, human-friendly
syntax.

Inspired by Adam Wiggins' article "Rethinking Cron" (Google cache) and the
clockwork Ruby module.

# {{{1 prep
%prep
%setup -q

# {{{1 build
%build
%{__python2} %{python_setup} build

# {{{1 install
%install
rm -rf %{buildroot}

%{__python2} %{python_setup} install -O1 --skip-build --root %{buildroot}

# {{{1 clean
%clean
rm -rf %{buildroot}

# {{{1 files
%files
%defattr(-,root,root,-)

%doc *.rst *.txt
%{python2_sitelib}/%{python_package_name}*egg-info
%{python2_sitelib}/%{python_package_name}/

# {{{1 changelog
%changelog
