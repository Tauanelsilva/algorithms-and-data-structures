#include <cassert>
#include <iostream>
#include <vector>

std::vector<int> merge(const std::vector<int>& left, const std::vector<int>& right) {
    std::vector<int> merged;
    std::size_t i = 0;
    std::size_t j = 0;
    while (i < left.size() && j < right.size()) {
        if (left[i] <= right[j]) {
            merged.push_back(left[i++]);
        } else {
            merged.push_back(right[j++]);
        }
    }
    merged.insert(merged.end(), left.begin() + static_cast<std::ptrdiff_t>(i), left.end());
    merged.insert(merged.end(), right.begin() + static_cast<std::ptrdiff_t>(j), right.end());
    return merged;
}

std::vector<int> merge_sort(const std::vector<int>& values) {
    if (values.size() <= 1) {
        return values;
    }
    const std::size_t middle = values.size() / 2;
    const std::vector<int> left = merge_sort({values.begin(), values.begin() + static_cast<std::ptrdiff_t>(middle)});
    const std::vector<int> right = merge_sort({values.begin() + static_cast<std::ptrdiff_t>(middle), values.end()});
    return merge(left, right);
}

int binary_search(const std::vector<int>& values, int target) {
    int low = 0;
    int high = static_cast<int>(values.size()) - 1;
    while (low <= high) {
        const int middle = low + (high - low) / 2;
        if (values[middle] == target) {
            return middle;
        }
        if (values[middle] < target) {
            low = middle + 1;
        } else {
            high = middle - 1;
        }
    }
    return -1;
}

int main() {
    const std::vector<int> sorted = merge_sort({4, 1, 3, 2, 2});
    assert((sorted == std::vector<int>{1, 2, 2, 3, 4}));
    assert(binary_search(sorted, 2) == 1);
    assert(binary_search(sorted, 8) == -1);
    std::cout << "ok\n";
    return 0;
}
