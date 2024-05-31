export const searchResultModel = ({
  rank = "",
  text = "",
  score = "",
  docId = "",
}) => ({
  rank,
  text,
  docId,
  score,
});
