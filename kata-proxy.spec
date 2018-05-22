#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : kata-proxy
Version  : 1.0.0
Release  : 1
URL      : https://github.com/kata-containers/proxy/archive/1.0.0.tar.gz
Source0  : https://github.com/kata-containers/proxy/archive/1.0.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause ISC MIT MPL-2.0-no-copyleft-exception
Requires: kata-proxy-bin
BuildRequires : go
Patch1: 0001-add-fake-autogen.patch

%description
[![Build Status](https://travis-ci.org/kata-containers/proxy.svg?branch=master)](https://travis-ci.org/kata-containers/proxy)
[![codecov](https://codecov.io/gh/kata-containers/proxy/branch/master/graph/badge.svg)](https://codecov.io/gh/kata-containers/proxy)

%package bin
Summary: bin components for the kata-proxy package.
Group: Binaries

%description bin
bin components for the kata-proxy package.


%prep
%setup -q -n proxy-1.0.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1527003705
%autogen --disable-static ;export GOPATH="${PWD}/gopath/" \
;mkdir -p "${GOPATH}/src/github.com/kata-containers/" \
;ln -sf "${PWD}" "${GOPATH}/src/github.com/kata-containers/shim" \
;cd "${GOPATH}/src/github.com/kata-containers/shim"
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1527003705
rm -rf %{buildroot}
%make_install LIBEXECDIR=%{buildroot}//usr/libexec/

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/libexec/kata-containers/kata-proxy
