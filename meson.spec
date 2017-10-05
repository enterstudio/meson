Name: meson
Version: 0.42.1
Release: 1
Source0: https://github.com/mesonbuild/meson/archive/%{version}.tar.gz
Summary: A build system
URL: http://mesonbuild.com/
License: Apache 2
Group: Development/Tools
Requires: ninja
Requires: python >= 3.0
BuildRequires: python >= 3.0
BuildRequires: python-setuptools
BuildArch: noarch

%description
Meson is an open source build system meant to be both extremely fast, and,
even more importantly, as user friendly as possible.

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%{_bindir}/*
%{_prefix}/lib/python*/site-packages/meson*
%{_mandir}/*/*
