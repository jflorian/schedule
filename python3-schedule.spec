# vim: foldmethod=marker

%global python_package_name schedule
%global python_setup setup.py

Name:           python3-schedule

# see HISTORY.rst
Version:        0.6.0
Release:        1%{?dist}

# {{{1 package meta-data
Summary:        Python job scheduling for humans

Group:          Development/Libraries
Vendor:         doubledog.org
License:        MIT
URL:            http://www.doubledog.org/git/%{name}/
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel

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
* Sun Mar 17 2019 John Florian <jflorian@doubledog.org> 0.6.0-1
- Change - [tito] freshen release targets (jflorian@doubledog.org)
- Bump version to 0.6.0 (mail@dbader.org)
- Clean up error messages (mail@dbader.org)
- Change hour validation (39542938+ConnorSkees@users.noreply.github.com)
- Missed quotes (39542938+ConnorSkees@users.noreply.github.com)
- Use single quotes instead of double quotes
  (39542938+ConnorSkees@users.noreply.github.com)
- Add Connor Skees to the list of authors
  (39542938+ConnorSkees@users.noreply.github.com)
- Add `pass` to emphasize empty class
  (39542938+ConnorSkees@users.noreply.github.com)
- Fix hour if statement (39542938+ConnorSkees@users.noreply.github.com)
- Properly test latest > interval
  (39542938+ConnorSkees@users.noreply.github.com)
- Delete more duplicated code (39542938+ConnorSkees@users.noreply.github.com)
- Remove duplicated code (39542938+ConnorSkees@users.noreply.github.com)
- Remove unreachable code (39542938+ConnorSkees@users.noreply.github.com)
- Finish reverting changes (39542938+ConnorSkees@users.noreply.github.com)
- Revert unittest changes (39542938+ConnorSkees@users.noreply.github.com)
- Improve coverage (39542938+ConnorSkees@users.noreply.github.com)
- Properly test invalid hours/minutes/seconds
  (39542938+ConnorSkees@users.noreply.github.com)
- Missed a line (39542938+ConnorSkees@users.noreply.github.com)
- Fix line lengths to be under 80
  (39542938+ConnorSkees@users.noreply.github.com)
- Test more raises (39542938+ConnorSkees@users.noreply.github.com)
- Properly implement context managers with assertRaises
  (39542938+ConnorSkees@users.noreply.github.com)
- More descriptive assertions (39542938+ConnorSkees@users.noreply.github.com)
- Test interval errors more comprehensively
  (39542938+ConnorSkees@users.noreply.github.com)
- Improve test coverage (39542938+ConnorSkees@users.noreply.github.com)
- Change exception assertions to context managers
  (39542938+ConnorSkees@users.noreply.github.com)
- Test interval errors (39542938+ConnorSkees@users.noreply.github.com)
- Make linter happy :) (39542938+ConnorSkees@users.noreply.github.com)
- Line lengths under 80 characters
  (39542938+ConnorSkees@users.noreply.github.com)
- Unit tests under 79 characters
  (39542938+ConnorSkees@users.noreply.github.com)
- Update unit tests to reflect new exceptions
  (39542938+ConnorSkees@users.noreply.github.com)
- ValueError to ScheduleValueError
  (39542938+ConnorSkees@users.noreply.github.com)
- Change time assertions to ScheduleValueError
  (39542938+ConnorSkees@users.noreply.github.com)
- Change ValueError to ScheduleValueError
  (39542938+ConnorSkees@users.noreply.github.com)
- 2 lines between classes (39542938+ConnorSkees@users.noreply.github.com)
- Change interval assertions to IntervalError
  (39542938+ConnorSkees@users.noreply.github.com)
- Missed == to != (39542938+ConnorSkees@users.noreply.github.com)
- Add more descriptive exceptions
  (39542938+ConnorSkees@users.noreply.github.com)
- Fix line length to be 79 characters
  (39542938+ConnorSkees@users.noreply.github.com)
- Add assertion error messages (39542938+ConnorSkees@users.noreply.github.com)
- Get the line length below 80 (nathan.wailes@gmail.com)
- Add Nathan Wailes to the list of authors (nathan.wailes@gmail.com)
- Update FAQ.rst (mail@dbader.org)
- Make the at() docstring more descriptive (nathan.wailes@gmail.com)
- Don't allow whitespace in the string passed to at() (nathan.wailes@gmail.com)
- Remove two unnecessary tests (nathan.wailes@gmail.com)
- Check the at() format based on the selected units (nathan.wailes@gmail.com)
- Raise an exception if at() is not passed a string in the right format
  (nathan.wailes@gmail.com)
- Update the READMEs now that the two-colon every().minute.at('::SS') syntax
  has been removed (nathan.wailes@gmail.com)
- Fix a bug where the at(':SS') syntax wasn't working (nathan.wailes@gmail.com)
- Remove unnecessary tests (nathan.wailes@gmail.com)
- Make the at() function easier to read (nathan.wailes@gmail.com)
- Update the at() docstring to reflect its new abilities
  (nathan.wailes@gmail.com)
- Support recurring tasks in the form "every().minute.at('::30')"
  (nathan.wailes@gmail.com)
- Get the code's line lengths below 80 (nathan.wailes@gmail.com)
- Make at() accept timestamps with 1 second precision (nathan.wailes@gmail.com)
- Ignore the .idea/ directory used by PyCharm (nathan.wailes@gmail.com)
- Link to LICENSE directly (karl.coelho1@gmail.com)
- Disable Python 3.7 builds again (mail@dbader.org)
- Fix CI build (hello@dbader.org)
- Add Python3.7 to CI tests (alx.kuzm@gmail.com)
- Update sidebarintro.html (hello@dbader.org)
- Update schedule/__init__.py (chenxuefeng1207@163.com)
- Fix incorrect code sample in FAQs (29029116+aydwi@users.noreply.github.com)
- Sync Docstring with README (waydi1@gmail.com)
- Update FAQ.rst (hello@dbader.org)
- Update README.rst (hello@dbader.org)
- Remove duplicate tags type check (mail@dbader.org)
- Fix coverage command (mail@dbader.org)
- Ensure failed coveralls run fails the build (mail@dbader.org)
- Fix coverage tracking (mail@dbader.org)

* Wed Nov 29 2017 John Florian <jflorian@doubledog.org> 0.5.0-1
- new package built with tito

* Tue Aug 09 2016 John Florian <jflorian@doubledog.org> 0.3.2-2
- New - tito releaser for Fedora 24 (jflorian@doubledog.org)

* Mon Jun 06 2016 John Florian <jflorian@doubledog.org> 0.3.2-1
- new package built with tito

