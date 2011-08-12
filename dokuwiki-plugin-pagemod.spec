%define		plugin		pagemod
%define		php_min_version 5.0.0
%include	/usr/lib/rpm/macros.php
Summary:	Plugin to add information to pages in a structured way (via forms)
Name:		dokuwiki-plugin-%{plugin}
Version:	1.2
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://freecode.baselineit.net/dokuwiki/pagemod-%{version}.zip
# Source0-md5:	8809490c0c9cc692506f7f57b5910769
URL:		http://www.dokuwiki.org/plugin:pagemod
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.520
Requires:	dokuwiki >= 20091225
Requires:	dokuwiki-plugin-bureaucracy
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-date
Requires:	php-pcre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}
%define		bplugindir	%{dokudir}/lib/plugins/bureaucracy

%description
A plugin which allows you to add information to pages in a structured
way (via forms), it works with the bureaucracy plugin.

%prep
%setup -qc

version=$(awk -F"'" '/date/&&/=>/{print $4}' %{plugin}/syntax.php)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
#	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{plugindir},%{bplugindir}}
cp -a %{plugin}/* $RPM_BUILD_ROOT%{plugindir}
cp -a bureaucracy/* $RPM_BUILD_ROOT%{bplugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{plugindir}
%{plugindir}/*.php
%{bplugindir}/actions/*.php
