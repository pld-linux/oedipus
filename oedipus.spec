Summary:	The Oedipus Web Scanner Project
Summary(pl):	Oedipus - narzêdzie do skanowania aplikacji WWW
Name:		oedipus
Version:	1.7.4.1
Release:	0.1
License:	GPL v2+
Group:		Applications
Source0:	http://rubyforge.org/frs/download.php/8639/oedipus-alpha-1_7_4_1.tar.gz
# Source0-md5:	7f4dd33f0506da1257597b09d87a88d9
URL:		http://oedipus.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-RubyGems
BuildRequires:	sed >= 4.0
%{?ruby_mod_ver_requires_eq}
Requires:	ruby-RubyGems
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		gemsdir		%{_libdir}/ruby/gems/%{ruby_version}
%define		pkgdir		%{_datadir}/%{name}

%description
Oedipus is an open source web application security analysis and
testing suite.

%description -l pl
Oedipus to zestaw narzêdzi do analizy i testów bezpieczeñstwa
aplikacji WWW.

%prep
%setup -q -n oedipus-alpha-1_7_4_1

sed -i -e 's,/usr/local/bin/ruby,/usr/bin/ruby,' o_analyzer.rb o_scanner.rb

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{gemsdir},%{pkgdir}}

cp -a *.rb analyzer reporter scanner tools $RPM_BUILD_ROOT%{pkgdir}

cd docs/install
gem install PluginFactory-1.0.1 -i $RPM_BUILD_ROOT%{gemsdir}
gem install builder-2.0.0 -i $RPM_BUILD_ROOT%{gemsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README docs/{BUGS,TODO,USAGE,changelog.txt}
#%attr(755,root,root) %{_bindir}/*
%dir %{pkgdir}
%attr(755,root,root) %{pkgdir}/o_analyzer.rb
%attr(755,root,root) %{pkgdir}/o_scanner.rb
%{pkgdir}/analyzer*
%{pkgdir}/reporter*
%{pkgdir}/scanner*
%{pkgdir}/tools
%{gemsdir}/doc/PluginFactory-*
%{gemsdir}/doc/builder-*
%{gemsdir}/gems/PluginFactory-*
%{gemsdir}/gems/builder-*
%{gemsdir}/specifications/PluginFactory-*.gemspec
%{gemsdir}/specifications/builder-*.gemspec
