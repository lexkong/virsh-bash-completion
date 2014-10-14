%define name virsh-bash-completion
%define version 0.1
Name:           virsh-bash-completion
Version:        0.1
Release:        1
Summary:        This is a libvirt virsh command completion script.
Group:          Applications/Tools
License:        GPL  
URL:            https://github.com/alex8866/deploy.git
Source0:        virsh-bash-completion-0.1.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)  
#BuildRequires:   
Requires:       libvirt-client
Requires:       bash-completion
%description  
virsh-bash-completion is a libvirt virsh command completion script.

%prep  
rm -rf %{_builddir}/%{name}-%{version}
mkdir -p %{buildroot}  
echo buildroot: %{buildroot}  
%setup -q  
%install  
echo builddir: %{_builddir}
cd %{_builddir}/
mkdir -p %{buildroot}/usr/share/bash-completion/completions
cp %{name}-%{version}/%{name} %{buildroot}/usr/share/bash-completion/completions/virsh
#cp %{buildroot}/usr/local/src/%{name}-%{version}/conf/.bashrc %{buildroot}/usr/local/src/%{name}-%{version}/conf/.profile
%clean  
rm -rf %{buildroot}
%files  
%defattr(-,root,root,-)  
/usr/share/bash-completion/completions/virsh
%doc  
