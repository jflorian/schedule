# vim: foldmethod=marker

%global python_package_name schedule
%global python_setup setup.py

Name:           python3-schedule

# see HISTORY.rst
Version:        1.1.0
Release:        2%{?dist}

# {{{1 package meta-data
Summary:        Python job scheduling for humans

Group:          Development/Libraries
Vendor:         doubledog.org
License:        MIT
URL:            http://www.doubledog.org/git/%{name}/
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

Requires:       python%{python3_pkgversion}

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
%{__python3} %{python_setup} build

# {{{1 install
%install

%{__python3} %{python_setup} install -O1 --skip-build --root %{buildroot}

# {{{1 files
%files

%doc *.rst *.txt
%{python3_sitelib}/%{python_package_name}*egg-info
%{python3_sitelib}/%{python_package_name}/

# {{{1 changelog
%changelog
* Mon Feb 07 2022 John Florian <jflorian@doubledog.org> 1.1.0-2
- Bug - [spec] missing dep on setuptools (jflorian@doubledog.org)

- Release 1.1.0 (sijmenhuizenga@gmail.com)
- Update version string conf.py to current version (#453)
  (sijmenhuizenga@gmail.com)
- Module Queue should be queue (#448) (sijmenhuizenga@gmail.com)
- Split up Github Actions (#442) (sijmenhuizenga@gmail.com)
- Add execute until functionality (#195) (me@fredthomsen.net)
- Add more explanatory message on IntervalError exception (#439)
  (pedrochaveslimas3@gmail.com)
- Fix typos in __init__.py (#437) (70908187+ebllg@users.noreply.github.com)
- include changelog in html docs (#436)
  (70908187+ebllg@users.noreply.github.com)
- Add more descriptive error messages (#280)
  (39542938+connorskees@users.noreply.github.com)
- Fix typos in 'multiple schedulers' docs (#435) (sijmenhuizenga@gmail.com)
- Add type annotations (#427) (info@martin-thoma.de)
- Reformat code using Black formatter (#432) (info@martin-thoma.de)
- Added zcking to authors (sijmenhuizenga@gmail.com)
- Update logging docs (sijmenhuizenga@gmail.com)
- Remove default logger configuration (sijmenhuizenga@gmail.com)
- Installation instructions cleanup + added conda  (#421)
  (sijmenhuizenga@gmail.com)
- Fix str of job when there is no __name__ (#430) (avery@averyjfischer.com)
- Added a decorator (#148) (ramonhagenaars@gmail.com)
- Fix typo in examples.rst (#426) (sijmenhuizenga@gmail.com)
- Update GitHub button in docs (mail@dbader.org)
- Added way to retrieve jobs per tags (#419)
  (17214791+Skenvy@users.noreply.github.com)
- Release v1.0.0 (#418) (SijmenHuizenga@users.noreply.github.com)
- Move and update deployment docs into development.rst (#417)
  (SijmenHuizenga@users.noreply.github.com)
- Drop python 2.7 and 3.5, add python 3.9 (#416)
  (SijmenHuizenga@users.noreply.github.com)
- Fix hour.at('MM:SS') parsing bug (#290) (Elad.Birnboim@microsoft.com)
- Fix coveralls after update to 3.0.0 (sijmenhuizenga@gmail.com)
- Make long-running jobs not skip periods (sijmenhuizenga@gmail.com)
- Improve docs of .at() method to better show allowed options
  (sijmenhuizenga@gmail.com)
- Make idle_seconds explicitly return None in case of no scheduled jobs (#401)
  (SijmenHuizenga@users.noreply.github.com)
- Fix import of queue (#306) (chankey007@gmail.com)
- Add example and unit test for idle_seconds() (#399)
  (SijmenHuizenga@users.noreply.github.com)
- Revamp and extend documentation (#395)
  (SijmenHuizenga@users.noreply.github.com)
- Log all messages as debug (sijmenhuizenga@gmail.com)
- Add seconds example to readme (#170) (vubon.roy@gmail.com)
- Replace Travis with Github Actions (#398)
  (SijmenHuizenga@users.noreply.github.com)
- Bugfix: tuesday.at('HH:MM:SS') where HMS=now+10s doesn't run today #331
  (#337) (pawel@kumor.it)
- Mute logging (aisk1988@gmail.com)
- Issue #296: DeprecationWarning. Fix working in python2.7 and 3.7
  (garikoitz1988@gmail.com)
- Issue #296:  DeprecationWarning 'collections' (garikoitz1988@gmail.com)
- Improve testing (mim@mim.pw)
- Test repr when at_time is not None
  (39542938+ConnorSkees@users.noreply.github.com)
- Surround function in blank lines
  (39542938+ConnorSkees@users.noreply.github.com)
- Linter is not a fan of lambdas
  (39542938+ConnorSkees@users.noreply.github.com)
- Update string tests (39542938+ConnorSkees@users.noreply.github.com)
- Add tests for repr (39542938+ConnorSkees@users.noreply.github.com)
- Make repr non-recursive (39542938+ConnorSkees@users.noreply.github.com)
- Add __str__ to Job (39542938+ConnorSkees@users.noreply.github.com)
- line break for flake8 check (kingzach77@gmail.com)
- default config added to logger; logs added for job clearing/cancelling
  (kingzach77@gmail.com)

