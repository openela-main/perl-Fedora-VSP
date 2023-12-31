Name:           perl-Fedora-VSP
Version:        0.001
Release:        10%{?dist}
Summary:        Perl version normalization for RPM
License:        GPLv3+
Group:          Development/Libraries
URL:            https://ppisar.fedorapeople.org/Fedora-VSP/
Source0:        %{url}Fedora-VSP-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
%if !%{defined perl_bootstrap}
# Break build cycle: perl-Fedora-VSP → perl-generators → perl-Fedora-VSP
BuildRequires:  perl-generators
%endif
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More)
BuildRequires:  perl(version)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
%if %{defined perl_bootstrap}
# Break build cycle: perl-Fedora-VSP → perl-generators → perl-Fedora-VSP
Requires:       perl(strict)
Requires:       perl(warnings)
Provides:       perl(Fedora::VSP) = %{version}
%endif

%description
This module provides functions for normalizing Perl version strings for
Red Hat Package (RPM) based Linux distributions.

%prep
%setup -q -n Fedora-VSP-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license COPYING
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Mar 29 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.001-10
- Rebuild with enable hardening (bug #1636329)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.001-7
- Perl 5.26 re-rebuild of bootstrapped packages

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.001-6
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 30 2016 Petr Pisar <ppisar@redhat.com> - 0.001-4
- Break build cycle when bootstrapping: perl-Fedora-VSP → perl-generators
  → perl-Fedora-VSP

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.001-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 09 2015 Petr Pisar <ppisar@redhat.com> 0.001-1
- First package
