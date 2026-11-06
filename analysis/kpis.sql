   -- number of cases per process
   SELECT process, COUNT(*) FROM postrueckl.cases GROUP BY process;

   -- total cost per process
   SELECT process, SUM(cost) FROM postrueckl.cases GROUP BY process;

   -- average cost per case per process
   SELECT process, AVG(cost) FROM postrueckl.cases GROUP BY process;

   -- cases resolved for free (after process)
   SELECT COUNT(*) FROM postrueckl.cases WHERE outcome = 'resolved_free';

   -- redundant lookups (before process)
   SELECT COUNT(*) FROM postrueckl.cases WHERE redundant = 1;