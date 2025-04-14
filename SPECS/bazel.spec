%undefine __brp_mangle_shebangs
%global _missing_build_ids_terminate_build 0
%global debug_package %{nil}

# Turn off strip'ng of binaries
%global __strip /bin/true

Name:           bazel
Version:        8.2.0
Release:        1%{?dist}
Summary:        a fast, scalable, multi-language and extensible build system
License:        Apache-2.0
URL:            https://bazel.build
Source0:        https://github.com/bazelbuild/bazel/releases/download/%{version}/bazel-%{version}-linux-x86_64

%description
%{summary}.

%install
install -Dm0644 %{SOURCE0} %{buildroot}/usr/bin/%{name}
chmod +x %{buildroot}/usr/bin/%{name}

%files
%defattr(-,root,root,-)
/usr/bin/%{name}

%changelog
* Tue Apr 15 2025 Jamie Curnow <jc@jc21.com> - 8.2.0-1
- v8.2.0

* Wed Feb 26 2025 Jamie Curnow <jc@jc21.com> - 8.1.1-1
- v8.1.1

* Mon Feb 24 2025 Jamie Curnow <jc@jc21.com> - 8.1.0-1
- v8.1.0
