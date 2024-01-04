%global _empty_manifest_terminate_build 0
Name:		python-gatt
Version:	0.2.7
Release:	1
Summary:	Bluetooth GATT SDK for Python
License:	MIT
URL:		https://github.com/getsenic/gatt-python
Source0:	https://mirrors.aliyun.com/pypi/web/packages/96/d0/d66154053d5b47996731d80ee66f65bdf7b790258addc0b6a5f50bcc3579/gatt-0.2.7.tar.gz
BuildArch:	noarch


%description


%package -n python3-gatt
Summary:	Bluetooth GATT SDK for Python
Provides:	python-gatt
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-pip
%description -n python3-gatt


%package help
Summary:	Development documents and examples for gatt
Provides:	python3-gatt-doc
%description help


%prep
%autosetup -n gatt-0.2.7

%build
%py3_build

%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
	find usr/lib -type f -printf "\"/%h/%f\"\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
	find usr/lib64 -type f -printf "\"/%h/%f\"\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
	find usr/bin -type f -printf "\"/%h/%f\"\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
	find usr/sbin -type f -printf "\"/%h/%f\"\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
	find usr/share/man -type f -printf "\"/%h/%f.gz\"\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%files -n python3-gatt -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Tue Jun 20 2023 Python_Bot <Python_Bot@openeuler.org> - 0.2.7-1
- Package Spec generated
