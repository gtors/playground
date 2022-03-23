function list_append(rec, bin, value)
  local l = rec[bin]
  list.append(l, value)
  rec[bin] = l
  aerospike:update(rec)
  return 0
end
