
1. Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
```java
class Solution {
    public String restoreString(String s, int[] indices) {
        int n=s.length(); // finding length of string
        char[] result = new char[n]; // declaring a new char array to store result
        for(int i=0;i<n;i++){
            result[indices[i]]=s.charAt(i);
        }
        return String.valueOf(result); // returning result
    }
}
```

1389. Create Target Array in the Given Order

```java
class Solution {
    public int[] createTargetArray(int[] nums, int[] index) {
        ArrayList<Integer> ansList = new ArrayList<Integer>();
        for (int i=0; i<nums.length; i++) {
            ansList.add(index[i], nums[i]);
        }
        int[] ans = new int[nums.length];
        for (int i=0; i<nums.length; i++) {
            ans[i] = ansList.get(i);
        }
        return ans;
    }
}
```


1913. Maximum Product Difference Between Two Pairs
```java
class Solution {
    public int maxProductDifference(int[] nums) {
        Arrays.sort(nums);
        return nums[nums.length-1]*nums[nums.length-2] - nums[0]*nums[1];
    }
}
```

804. Unique Morse Code Words
```java
class Solution {
    public int uniqueMorseRepresentations(String[] words) {
        String[] MORSE = new String[]{".-","-...","-.-.","-..",".","..-.","--.",
                         "....","..",".---","-.-",".-..","--","-.",
                         "---",".--.","--.-",".-.","...","-","..-",
                         "...-",".--","-..-","-.--","--.."};

        Set<String> seen = new HashSet();
        for (String word: words) {
            StringBuilder code = new StringBuilder();
            for (char c: word.toCharArray())
                code.append(MORSE[c - 'a']);
            seen.add(code.toString());
        }

        return seen.size();
    }
}
```


1748. Sum of Unique Elements
```java
class Solution {
    public int sumOfUnique(int[] nums) {
        int ans = 0;
        HashMap<Integer, Integer> cache = new HashMap<Integer, Integer>();
        for (int num:nums) {
            cache.put(num, cache.getOrDefault(num,0)+1);
        }
        
        for (Map.Entry<Integer, Integer> entry:cache.entrySet()) {
            if (entry.getValue() == 1) {
                ans += entry.getKey();
            }
        }
        
        return ans;
    }
}
```

1347. Minimum Number of Steps to Make Two Strings Anagram
```java
class Solution {
    public int minSteps(String s, String t) {
        int[] difference = new int[26];
        int n = s.length();
        int ans = 0;
        for (int i=0; i<n; i++) {
            difference[s.charAt(i)-'a']++;
            difference[t.charAt(i)-'a']--;
        }
        for (int num:difference) {
            if (num>0) {
                ans += num;
            }
        }
        return ans;
    }
}
```

1325. Delete Leaves With a Given Value
```java
class Solution {
    public TreeNode removeLeafNodes(TreeNode root, int target) {
        if (root.left != null) root.left = removeLeafNodes(root.left, target);
        if (root.right != null) root.right = removeLeafNodes(root.right, target);
        return root.left == root.right && root.val == target ? null : root;   
    }
}
```

1315. Sum of Nodes with Even-Valued Grandparent
```java
class Solution {
    
    public int sumEvenGrandparent(TreeNode root) {
        return helper(root, 1, 1);
    }

    public int helper(TreeNode node, int p, int gp) {
        if (node == null) return 0;
        return helper(node.left, node.val, p) + helper(node.right, node.val, p) + (gp % 2 == 0 ? node.val : 0);
    }
    
}
```
