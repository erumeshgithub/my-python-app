#!/bin/bash
echo "Testing Linux build environment locally..."

# Check Linux dependencies
check_dependency() {
    if command -v $1 &> /dev/null; then
        echo "✅ $1: $(which $1)"
        return 0
    else
        echo "❌ $1: NOT FOUND"
        return 1
    fi
}

echo "=== Linux Dependency Check ==="
check_dependency python3 || exit 1
check_dependency pip3 || exit 1
check_dependency git || exit 1
check_dependency java || exit 1
check_dependency zip || exit 1

echo "=== Python Environment ==="
python3 --version
pip3 --version

echo "=== Disk Space ==="
df -h .

echo "=== Project Structure ==="
tree -a

echo "=== File Contents ==="
echo "main.py:"
head -10 main.py
echo ""
echo "buildozer.spec:"
head -10 buildozer.spec

echo "✅ Local Linux environment is ready for GitHub Actions"
echo ""
echo "Next steps:"
echo "1. Create a GitHub repository"
echo "2. Run: git add ."
echo "3. Run: git commit -m 'Linux APK build setup'"
echo "4. Run: git push origin main"
