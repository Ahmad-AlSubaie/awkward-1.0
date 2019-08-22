// BSD 3-Clause License; see https://github.com/jpivarski/awkward-1.0/blob/master/LICENSE

#ifndef AWKWARD_LISTOFFSETARRAYCONTENT_H_
#define AWKWARD_LISTOFFSETARRAYCONTENT_H_

#include <sstream>
#include <memory>

#include "awkward/util.h"
#include "awkward/Index.h"
#include "awkward/Content.h"

#include <iostream>

namespace awkward {
  class ListOffsetArray: public Content {
  public:
    ListOffsetArray(const Index offsets, const std::shared_ptr<Content> content)
        : offsets_(offsets)
        , content_(content) {
          std::cout << "ListOffsetArray constructor" << std::endl;
        }

    ~ListOffsetArray() {
      std::cout << "ListOffsetArray destructor" << std::endl;
    }

    const Index offsets() const { return offsets_; }
    const std::shared_ptr<Content> content() const { return content_; }

    virtual const std::string repr(const std::string indent, const std::string pre, const std::string post) const;
    virtual std::shared_ptr<Content> get(AtType at) const;
    virtual std::shared_ptr<Content> slice(AtType start, AtType stop) const;

  private:
    const Index offsets_;
    const std::shared_ptr<Content> content_;
  };
}

#endif // AWKWARD_LISTOFFSETARRAYCONTENT_H_
