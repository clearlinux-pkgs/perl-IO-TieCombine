#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-IO-TieCombine
Version  : 1.005
Release  : 3
URL      : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/IO-TieCombine-1.005.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/IO-TieCombine-1.005.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libi/libio-tiecombine-perl/libio-tiecombine-perl_1.005-1.debian.tar.xz
Summary  : 'produce tied (and other) separate but combined variables'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-IO-TieCombine-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This archive contains the distribution IO-TieCombine,
version 1.005:
produce tied (and other) separate but combined variables

%package dev
Summary: dev components for the perl-IO-TieCombine package.
Group: Development
Provides: perl-IO-TieCombine-devel = %{version}-%{release}

%description dev
dev components for the perl-IO-TieCombine package.


%package license
Summary: license components for the perl-IO-TieCombine package.
Group: Default

%description license
license components for the perl-IO-TieCombine package.


%prep
%setup -q -n IO-TieCombine-1.005
cd ..
%setup -q -T -D -n IO-TieCombine-1.005 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/IO-TieCombine-1.005/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-IO-TieCombine
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-IO-TieCombine/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1IO/TieCombine.pm
/usr/lib/perl5/vendor_perl/5.28.1IO/TieCombine/Handle.pm
/usr/lib/perl5/vendor_perl/5.28.1IO/TieCombine/Scalar.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/IO::TieCombine.3
/usr/share/man/man3/IO::TieCombine::Handle.3
/usr/share/man/man3/IO::TieCombine::Scalar.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-IO-TieCombine/LICENSE
