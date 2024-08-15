Name:           protonmail
Version:        1.0.6
Release:        1%{?dist}
Summary:        The ProtonMail desktop email and calendar client

License:        GPL-3.0 
URL:            https://proton.me/mail
Source0:	https://github.com/ProtonMail/inbox-desktop/releases/download/%{version}/inbox-desktop-%{version}-source.zip 

BuildRequires:  nodejs
BuildRequires:  yarnpkg


## Install "dummy" apps to allow Proton's source code to build without modification. These are not actually required for building an RPM, but the build pipeline will fail without these packages.
BuildRequires:	fakeroot
BuildRequires:	dpkg
  

%description
The ProtonMail email and calendar client as an Electron application.

%prep
ls
unzip %{source} -d %{_builddir}/inbox-desktop-%{version}
ls
%autosetup


%build
yarn install
yarn run make --target=rpm

%configure
%make_build


%install
%make_install


%files
%license LICENSE



%changelog
* Wed Aug 14 2024 Seth Maurice-Brant <sethmb@pm.me>
- 
