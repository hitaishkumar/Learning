nums = [1,2,1]
nums.extend(nums)
st = []
ans = []
for i in range(len(nums)-1,-1,-1):
    if len(st) == 0:
        ans.append(-1)
        st.append(nums[i])
        continue
    if st[-1] > nums[i]:
        ans.append(st[-1])
        st.append(nums[i])
        continue
    else:
        while len(st) and st[-1] <= nums[i]:
            st.pop()
        if len(st):
            ans.append(st[-1])
        else:
            ans.append(-1)
        st.append(nums[i])
print(nums)
print(ans[::-1])()