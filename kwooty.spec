Summary:	A friendly NZB Usenet binary downloader
Name:		kwooty
Version:	1.0.1
Release:	3
License:	GPLv2+
Group:		Networking/News
Url:		https://kwooty.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/kwooty/%{name}-%{version}.tar.gz
BuildRequires:	cmake >= 2.6.0
BuildRequires:	kdebase4-workspace-devel >= 4.6.0
BuildRequires:	kdelibs4-devel >= 4.6.0
BuildRequires:	gettext
Requires:	p7zip
Requires:	parchive2
Requires:	unrar
Conflicts:	%{_lib}kwootycore0 < 1.0.1-2

%description
A friendly NZB newsgroup binary grabber. Its main features are:
- Automatic files verifying/repairing (par2 program required)
- Automatic archive extraction (unrar program required)
- Multi-server support
- Direct file downloading after opening a .nzb file
- Save/Restore pending downloads when application is closed/open
- System shutdown scheduling
- File queue and priority management
- SSL connection support
- Pause/Resume downloads.

%files -f %{name}.lang
%doc COPYING README.txt TODO
%{_kde_bindir}/%{name}
%{_kde_appsdir}/%{name}/*
%{_kde_applicationsdir}/%{name}.desktop
%{_kde_iconsdir}/hicolor/*/apps/%{name}.png
%{_kde_services}/%{name}_*.desktop
%{_kde_servicetypes}/%{name}*.desktop
%{_kde_datadir}/config.kcfg/%{name}*.kcfg
%{_kde_libdir}/kde4/%{name}_*.so

#----------------------------------------------------------------------------

%define major 0
%define libkwootycore %mklibname kwootycore %{major}

%package -n %{libkwootycore}
Summary:	Shared library for Kwooty Usenet binary grabber
Group:		System/Libraries

%description -n %{libkwootycore}
Shared library for Kwooty Usenet binary grabber.

%files -n %{libkwootycore}
%doc COPYING
%{_kde_libdir}/libkwootycore.so.%{major}*
# ugly file naming but SONAME is correct
%{_kde_libdir}/libkwootycore.so.%{version}

#----------------------------------------------------------------------------

%prep
%setup -q
# The build directory already exist:
# removing to avoid errors later from our build scripts
rmdir build

# Remove wrong file perms
chmod -x COPYING
chmod -x README.txt

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name}

# We don't need this because there are no headers anyway
rm -f %{buildroot}%{_kde_libdir}/libkwootycore.so

