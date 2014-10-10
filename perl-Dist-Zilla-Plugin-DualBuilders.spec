%define upstream_name    Dist-Zilla-Plugin-DualBuilders
%define upstream_version 1.001

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Allows use of Module::Build and ExtUtils::MakeMaker in a dzil dist
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Dist::Zilla::Role::InstallTool)
BuildRequires:	perl(Dist::Zilla::Role::PrereqSource)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Util::TypeConstraints)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
This plugin allows you to specify ModuleBuild and MakeMaker in your the
Dist::Zilla manpage _dist.ini_ and select only one as your prereq.
Normally, if this plugin is not loaded you will end up with both in your
prereq list and this is obviously not what you want!

	# In your dist.ini:
	[ModuleBuild]
	[MakeMaker] ; or [MakeMaker::Awesome], will work too :)
	[DualBuilders] ; needs to be specified *AFTER* the builders

This plugin accepts the following options:

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
%doc LICENSE README META.yml Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

