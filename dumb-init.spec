Name:           dumb-init
Version:        1.1.3
Release:        2%{?dist}
Summary:        Entry-point for containers that proxies signals

License:        MIT
URL:            https://github.com/Yelp/dumb-init
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  help2man

%description
dumb-init is a simple process supervisor and init system designed to run as
PID 1 inside minimal container environments (such as Docker).

* It can handle orphaned zombie processes.
* It can pass signals properly for simple containers.

%prep
%autosetup

%build
# if we are building a release then this is not needed
# make VERSION.h 
gcc %{optflags} %{__global_ldflags} -o %{name} %{name}.c 
help2man --no-discard-stderr --include debian/help2man --no-info --name '%{summary}' ./%{name} > %{name}.1

%install
install -Dpm0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dpm0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%doc %{_mandir}/man1/%{name}.1*

%changelog
* Mon Aug 15 2016 alsadi <alsadi@gmail.com> - 1.1.3-2
- initial packaging
