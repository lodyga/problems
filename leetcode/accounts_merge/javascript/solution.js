class DSU {
   /**
    * @param {number} N 
    */
   constructor(N) {
      this.size = Array(N).fill(1);
      this.parent = Array.from({ length: N }, (_, index) => index);
   };

   /**
    * @param {number} u 
    * @returns {number}
    */
   find(u) {
      while (u !== this.parent[u]) {
         this.parent[u] = this.parent[this.parent[u]];
         u = this.parent[u];
      }
      return u
   };

   /**
    * @param {number} u 
    * @param {number} v 
    * @returns {void}
    */
   union(u, v) {
      let pu = this.find(u);
      let pv = this.find(v);

      if (pu == pv) {
         return
      } else if (this.size[pu] < this.size[pv]) {
         [pu, pv] = [pv, pu];
      }
      this.size[pu] += this.size[pv];
      this.parent[pv] = pu;
   };
}

class Solution {
   /**
    * Time complexity: O(m⋅log(m))
    * Auxiliary space complexity: O(n + m)
    * Tags:
    *     n: accounts size
    *     m: emial total count
    * @param {string[][]} accounts
    * @return {string[][]}
    */
   accountsMerge(accounts) {
      const N = accounts.length;
      // {email: owner id, }
      const emailOwner = new Map();
      const dsu = new DSU(N);

      // Parse name and emails.
      for (let userId = 0; userId < accounts.length; userId++) {
         const account = accounts[userId];

         for (let emailIndex = 1; emailIndex < account.length; emailIndex++) {
            const email = account[emailIndex];

            if (emailOwner.has(email)) {
               const prevUserId = emailOwner.get(email);
               dsu.union(prevUserId, userId)
            } else {
               emailOwner.set(email, userId)
            }
         }
      }

      // Group emails to appropriate parents.
      const emailGroup = new Map();
      for (const [email, userId] of emailOwner.entries()) {
         const parent = dsu.find(userId);

         if (!emailGroup.has(parent)) {
            emailGroup.set(parent, []);
         }

         emailGroup.get(parent).push(email);
      }

      // Sort emails and prepend name.
      const res = [];
      for (const [userId, emails] of emailGroup) {
         const name = accounts[userId][0];
         res.push([name, ...emails.sort()]);
      }
      return res
   };
}


const accountsMerge = new Solution().accountsMerge;
console.log(new Solution().accountsMerge([["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com", "john00@mail.com"], ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]).sort().toString() === [["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"], ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]].sort().toString())
console.log(new Solution().accountsMerge([["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"], ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"], ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"], ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"], ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]]).sort().toString() === [["Ethan", "Ethan0@m.co", "Ethan4@m.co", "Ethan5@m.co"], ["Gabe", "Gabe0@m.co", "Gabe1@m.co", "Gabe3@m.co"], ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co", "Hanzo3@m.co"], ["Kevin", "Kevin0@m.co", "Kevin3@m.co", "Kevin5@m.co"], ["Fern", "Fern0@m.co", "Fern1@m.co", "Fern5@m.co"]].sort().toString())
console.log(new Solution().accountsMerge([["David", "David0@m.co", "David1@m.co"], ["David", "David3@m.co", "David4@m.co"], ["David", "David4@m.co", "David5@m.co"], ["David", "David2@m.co", "David3@m.co"], ["David", "David1@m.co", "David2@m.co"]]).sort().toString() === [["David", "David0@m.co", "David1@m.co", "David2@m.co", "David3@m.co", "David4@m.co", "David5@m.co"]].sort().toString())
console.log(new Solution().accountsMerge([["Lily", "Lily4@m.co", "Lily5@m.co"], ["Lily", "Lily8@m.co", "Lily9@m.co"], ["Lily", "Lily15@m.co", "Lily16@m.co"], ["Lily", "Lily19@m.co", "Lily20@m.co"], ["Lily", "Lily6@m.co", "Lily7@m.co"], ["Lily", "Lily10@m.co", "Lily11@m.co"], ["Lily", "Lily5@m.co", "Lily6@m.co"], ["Lily", "Lily13@m.co", "Lily14@m.co"], ["Lily", "Lily9@m.co", "Lily10@m.co"], ["Lily", "Lily1@m.co", "Lily2@m.co"], ["Lily", "Lily3@m.co", "Lily4@m.co"], ["Lily", "Lily2@m.co", "Lily3@m.co"], ["Lily", "Lily11@m.co", "Lily12@m.co"], ["Lily", "Lily7@m.co", "Lily8@m.co"], ["Lily", "Lily12@m.co", "Lily13@m.co"], ["Lily", "Lily18@m.co", "Lily19@m.co"], ["Lily", "Lily17@m.co", "Lily18@m.co"], ["Lily", "Lily16@m.co", "Lily17@m.co"], ["Lily", "Lily14@m.co", "Lily15@m.co"], ["Lily", "Lily0@m.co", "Lily1@m.co"]]).sort().toString() === [["Lily", "Lily0@m.co", "Lily10@m.co", "Lily11@m.co", "Lily12@m.co", "Lily13@m.co", "Lily14@m.co", "Lily15@m.co", "Lily16@m.co", "Lily17@m.co", "Lily18@m.co", "Lily19@m.co", "Lily1@m.co", "Lily20@m.co", "Lily2@m.co", "Lily3@m.co", "Lily4@m.co", "Lily5@m.co", "Lily6@m.co", "Lily7@m.co", "Lily8@m.co", "Lily9@m.co"]].sort().toString())
