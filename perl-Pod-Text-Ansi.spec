%define upstream_name    Pod-Text-Ansi
%define upstream_version 0.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Convert POD to ANSI-colored text
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Pod/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Pod::Text)
BuildRequires:	perl(Term::ANSIColor)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
Pod::Text::Ansi is a simple subclass of Pod::Text that highlights output
text using ANSI color escape sequences. Apart from the color, it in all
ways functions like Pod::Text. See the Pod::Text manpage for details and
available options.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.50.0-2mdv2011.0
+ Revision: 656823
- rebuild for updated spec-helper

* Mon Aug 23 2010 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2011.0
+ Revision: 572226
- update to 0.05

* Sun Aug 16 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.0
+ Revision: 416984
- update to 0.04

* Wed Jul 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2010.0
+ Revision: 396306
- import perl-Pod-Text-Ansi


* Wed Jul 15 2009 cpan2dist 0.03-1mdv
- initial mdv release, generated with cpan2dist
